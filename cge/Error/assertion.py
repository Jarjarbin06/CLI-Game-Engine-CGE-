#############################
###                       ###
###          CGE          ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_error import Error


class ErrorAssertion(Error):

    def __init__(
            self,
            message : str = "assertion not validated",

            *,
            link : tuple[str , int | None] | None = None
        ) -> None:
        """
            Create an Error.

            Parameters:
                message (str, optional): The error message.
                link (tuple[str, int | None] | None, optional): The link to where the error comes from (file and line).
        """

        self.message : str = message
        self.error : str = "\nErrorAssertion"
        self.link_data : tuple[str, int] | None = link
        self.link : str | None = None

        self.create_link()
        self.log()