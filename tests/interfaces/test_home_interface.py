import pytest
from typing import List, Dict, Any

from interfaces.home_interface import HomeRepository
from models.home_model import HomeWrite


class TestHomeRepository(HomeRepository):
    """
    A concrete implementation of the HomeRepository interface for testing.
    """
    def __init__(self):
        self.homes = {}
        self.is_closed = False

    def create_home(self, home_create: HomeWrite) -> str:
        home_id = "test-uuid"
        self.homes[home_id] = home_create
        return home_id

    def get_home(self, home_id: str) -> Dict[str, Any]:
        if home_id in self.homes:
            return {"uuid": home_id, "name": self.homes[home_id].name}
        return None

    def list_homes(self) -> List[Dict[str, Any]]:
        return [{"uuid": home_id, "name": home.name} for home_id, home in self.homes.items()]

    def update_home(self, home_id: str, home_update: HomeWrite) -> None:
        if home_id in self.homes:
            self.homes[home_id] = home_update

    def delete_home(self, home_id: str) -> None:
        if home_id in self.homes:
            del self.homes[home_id]

    def close(self) -> None:
        self.is_closed = True


def test_home_repository_interface():
    """
    Test that a concrete implementation of HomeRepository can be created
    and that it implements all the required methods.
    """
    # Create a concrete implementation
    repo = TestHomeRepository()

    # Test create_home
    home = HomeWrite(name="Test Home")
    home_id = repo.create_home(home)
    assert home_id == "test-uuid"

    # Test get_home
    retrieved_home = repo.get_home(home_id)
    assert retrieved_home["uuid"] == home_id
    assert retrieved_home["name"] == "Test Home"

    # Test list_homes
    homes = repo.list_homes()
    assert len(homes) == 1
    assert homes[0]["uuid"] == home_id
    assert homes[0]["name"] == "Test Home"

    # Test update_home
    updated_home = HomeWrite(name="Updated Home")
    repo.update_home(home_id, updated_home)
    retrieved_home = repo.get_home(home_id)
    assert retrieved_home["name"] == "Updated Home"

    # Test delete_home
    repo.delete_home(home_id)
    assert repo.get_home(home_id) is None

    # Test close
    repo.close()
    assert repo.is_closed


def test_home_repository_abstract_methods():
    """
    Test that HomeRepository cannot be instantiated directly
    because it has abstract methods.
    """
    with pytest.raises(TypeError) as exc:
        HomeRepository()

    assert "Can't instantiate abstract class HomeRepository" in str(exc.value)
    assert "abstract methods" in str(exc.value)