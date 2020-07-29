# from typing import Optional, Iterable, List
# from typing_extensions import Protocol, Type
#
#
# class Combiner(Protocol):
#     def __call__(self, *vals: bytes, maxlen: Optional[int] = None) -> List[bytes]: ...
#
# def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
#     for item in data:
#         ...
#
#
# def good_cb(*vals: bytes, a: int, maxlen: Optional[int] = None) -> List[bytes]:
#     ...
# def bad_cb(*vals: bytes, maxitems: Optional[int]) -> List[bytes]:
#     ...
#
# batch_proc([], good_cb)  # OK
# # batch_proc([], bad_cb)   # Error! Argument 2 has incompatible type because of
# #                          # different name and kind in the callback