from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee import Employee


T = TypeVar("T", bound="GetEmployeeResponse200")


@_attrs_define
class GetEmployeeResponse200:
    """
    Attributes:
        data (Union[Unset, Employee]):
    """

    data: Union[Unset, "Employee"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.employee import Employee

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, Employee]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Employee.from_dict(_data)

        get_employee_response_200 = cls(
            data=data,
        )

        get_employee_response_200.additional_properties = d
        return get_employee_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
