from watson_developer_cloud import AssistantV1, WatsonApiException

import WatsonMsgResponse
class watsonController:


    version=""
    username=""
    password=""
    url=""
    workspace=""
    watson_assistant= None

    def __init__(self,version, username,password,url,workspace):
        self.version=version
        self.username=username
        self.password=password
        self.url=url
        self.workspace=workspace
        init_assistant()

    def init_assistant(self):
        try:
            watson_assistant= AssistantV1(
                version=self.version,
                username=self.username,
                password=self.password,
                url=self.url
                )
        except WatsonApiException as ex:
            print "Method failed with status code " + str(ex.code) + ": " + ex.message

    def sendMessage(self,text,context=None,entities=None,intents=None, output=None):
        response = assistant.message(
            workspace_id=self.workspace,
            input={'text': text},
            context=context,
            entities=entities,
            intents=intents,
            output=output
            ).get_result()

        return WatsonMsgResponse(response)
