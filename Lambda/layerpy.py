import json
import boto3

def create_bedrock_client():
    """
    Create and return a Bedrock Runtime client using boto3.

    Returns:
    - boto3.client: Bedrock Runtime client.
    """
    bedrock = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-west-2"
    )
    return bedrock

def query_action(question, bedrock):
    """
    Query the Bedrock Claude model with a given user question.

    Args:
    - question (str): User's input/question.
    - bedrock (boto3.client): Bedrock Runtime client.

    Returns:
    - dict: Result from the Bedrock model.
    """
    prompt = f"""\n\nHuman: 
        {question}
        \n\nAssistant:
        """
    
    body = json.dumps(
        {
            "prompt": f"{prompt}",
            "max_tokens_to_sample": 300,
            "temperature": 1,
            "top_k": 250,
            "top_p": 0.99,
            "stop_sequences": [
                "\n\nHuman:"
            ],
            "anthropic_version": "bedrock-2023-05-31"
        }
    )
    modelId = "anthropic.claude-v2:1"
    contentType = "application/json"
    accept = "*/*"
        
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    result = json.loads(response.get("body").read())
    print(result)
    return result

def handle_fallback(event):
    """
    Handle the FallbackIntent by querying the Bedrock model with the user's input.

    Args:
    - event (dict): AWS Lambda event containing information about the Lex session.

    Returns:
    - dict: Lex response including the Bedrock model's completion.
    """
    slots = event["sessionState"]["intent"]["slots"]
    intent = event["sessionState"]["intent"]["name"]
    bedrock = create_bedrock_client()
    question = event["inputTranscript"]
    result = query_action(question, bedrock)
    session_attributes = event["sessionState"]["sessionAttributes"]

    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close",
            },
            "intent": {"name": intent, "slots": slots, "state": "Fulfilled"},
            "sessionAttributes": session_attributes,
        },
        "messages": [
            {"contentType": "PlainText", "content": result["completion"]},
        ],
    }
    return response

def lambda_handler(event, context):
    """
    AWS Lambda handler function.

    Args:
    - event (dict): AWS Lambda event.
    - context (object): AWS Lambda context.

    Returns:
    - dict: Lex response.
    """
    session_attributes = event["sessionState"]["sessionAttributes"]
    intent = event["sessionState"]["intent"]["name"]
    if intent == "FallbackIntent":
        return handle_fallback(event)