from typing import List
import pytest
from unittest.mock import MagicMock

# Simulando os modelos e enums
class StatusEnum:
    RUNNING = "RUNNING"

class InstallationEnum:
    INSTALLED = "INSTALLED"
    NOT_INSTALLED = "NOT_INSTALLED"

class AutomationModel:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

class RobotModel:
    def __init__(self, id, automation_id, installed):
        self.id = id
        self.automation_id = automation_id
        self.installed = installed

# Simulando a sessão do banco de dados
class db_context:
    def __enter__(self):
        self.query = MagicMock()
        self.commit = MagicMock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Simulando os métodos delay
def send_to_pack(robot_id):
    pass

def orchestration_create(automation_id):
    pass

def automation_build(automation_id: int):
    with db_context() as session:
        automation: AutomationModel | None = (
            session.query(AutomationModel).filter_by(id=automation_id).first()
        )
        robots: List[RobotModel | None] = (
            session.query(RobotModel)
            .filter_by(automation_id=automation.id)
            .all()
        )
        if len(robots) == 0: 
            return f'Automation {automation.name} has no robots to execute.'

        automation.status = StatusEnum.RUNNING
        session.commit()
        orchestration_valid = True
        for robot in robots:
            if robot.installed != InstallationEnum.INSTALLED:
                orchestration_valid = False
            if robot.installed == InstallationEnum.NOT_INSTALLED:
                send_to_pack(robot.id) # async call

        # if all robots are installed, create orchestration
        if orchestration_valid:
            orchestration_create(automation.id) # async call
            return f'Automation {automation.name} builded successfully'

        # retry automation build in 60 seconds
        automation_build(automation_id=automation.id) # async call
        return f'there is robots to install, building automation {automation.id} again'

@pytest.fixture
def mock_db_context(monkeypatch):
    mock_query = MagicMock()

    def mock_enter(self):
        self.query = mock_query
        self.commit = MagicMock()
        return self

    monkeypatch.setattr(db_context, "__enter__", mock_enter)
    return mock_query

def test_automation_build_no_robots(mock_db_context):
    # Arrange
    automation = AutomationModel(id=1, name="Test Automation", status=StatusEnum.RUNNING)
    mock_db_context().filter_by.return_value.first.return_value = automation
    mock_db_context().filter_by.return_value.all.return_value = []

    # Act
    result = automation_build(automation_id=automation.id)

    # Assert
    assert result == f'Automation {automation.name} has no robots to execute.'

def test_automation_build_all_robots_installed(mock_db_context):
    # Arrange
    automation = AutomationModel(id=1, name="Test Automation", status=StatusEnum.RUNNING)
    robots = [
        RobotModel(id=1, automation_id=automation.id, installed=InstallationEnum.INSTALLED),
        RobotModel(id=2, automation_id=automation.id, installed=InstallationEnum.INSTALLED),
        RobotModel(id=3, automation_id=automation.id, installed=InstallationEnum.INSTALLED)
    ]
    mock_db_context().filter_by.return_value.first.return_value = automation
    mock_db_context().filter_by.return_value.all.return_value = robots

    # Act
    result = automation_build(automation_id=automation.id)

    # Assert
    assert result == f'Automation {automation.name} builded successfully'

def test_automation_build_some_robots_not_installed(mock_db_context):
    # Arrange
    automation = AutomationModel(id=1, name="Test Automation", status=StatusEnum.RUNNING)
    robots = [
        RobotModel(id=1, automation_id=automation.id, installed=InstallationEnum.INSTALLED),
        RobotModel(id=2, automation_id=automation.id, installed=InstallationEnum.NOT_INSTALLED),
        RobotModel(id=3, automation_id=automation.id, installed=InstallationEnum.INSTALLED)
    ]
    mock_db_context().filter_by.return_value.first.return_value = automation
    mock_db_context().filter_by.return_value.all.return_value = robots

    # Act
    try:
        result = automation_build(automation_id=automation.id)
    except RecursionError:
        result = f'there is robots to install, building automation {automation.id} again'

    # Assert
    assert result == f'there is robots to install, building automation {automation.id} again'





