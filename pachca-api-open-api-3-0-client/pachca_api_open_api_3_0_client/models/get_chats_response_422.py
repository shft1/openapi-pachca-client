from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error import Error


T = TypeVar("T", bound="GetChatsResponse422")


@_attrs_define
class GetChatsResponse422:
    """
    Attributes:
        errors (Union[Unset, list['Error']]):
    """

    errors: Union[Unset, list["Error"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for componentsschemas_errors_item_data in self.errors:
                componentsschemas_errors_item = componentsschemas_errors_item_data.to_dict()
                errors.append(componentsschemas_errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.error import Error

        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for componentsschemas_errors_item_data in _errors or []:
            componentsschemas_errors_item = Error.from_dict(componentsschemas_errors_item_data)

            errors.append(componentsschemas_errors_item)

        get_chats_response_422 = cls(
            errors=errors,
        )

        get_chats_response_422.additional_properties = d
        return get_chats_response_422

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
