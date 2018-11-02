


class WatsonMsgResponse:

    input=None #The user input from the request.
    intents=None #An array of intents recognized in the user input, sorted in descending order of confidence.
    entities=None #An array of entities identified in the user input.
    alternate_intents=None #Whether to return more than one intent. A value of true indicates that all matching intents are returned.
    context=None #State information for the conversation.
    output=None #Output from the dialog, including the response to the user, the nodes that were triggered, and log messages.
    actions=None #An array of objects describing any actions requested by the dialog node.

    def __init__(self,response):
        if(response["input"]!=None):
            input=response["input"]
        if(response["intents"]!=None):
            input=response["intents"]
        if(response["entities"]!=None):
            input=response["entities"]
        if(response["alternate_intents"]!=None):
            input=response["alternate_intents"]
        if(response["context"]!=None):
            input=response["context"]
        if(response["actions"]!=None):
            input=response["actions"]
