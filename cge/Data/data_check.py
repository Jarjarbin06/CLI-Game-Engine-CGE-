#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from cge.Error.assertion import ErrorAssertion


def assertion(assertions: bool, message: str = "assertion not validated", file: str | None = None, line: int | None = None):
    try:
        assert isinstance(assertions, bool)
    except AssertionError:
        raise ErrorAssertion(message)
    if not assertions:
        raise ErrorAssertion(message, link=((file, line) if file else None))

