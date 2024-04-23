from random import choices, shuffle

from django.conf import settings


def get_invite_code() -> str:
    seq = list(settings.INVITE_CODE_CHARS)
    shuffle(seq)
    code = choices(seq, k=settings.INVITE_CODE_LENGTH)
    return "".join(code)


def get_confirmation_code() -> int:
    seq = list(map(lambda x: str(x), range(10)))
    shuffle(seq)
    code = choices(seq, k=settings.INVITE_CODE_LENGTH)
    return "".join(code)
