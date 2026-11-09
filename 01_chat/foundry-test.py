from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


endpoint = "https://yunzjo111-7861-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)


# #test case 1
# response = client.responses.create(
#     model=deployment_name,
#     input="What is the capital of France?",
# )
# print(response.output_text)

# #test case 2
# response = client.responses.create(
#     model="gpt-5-mini",  # Your model deployment name
#     input="What is Microsoft Foundry?"
# )
# print(response.output_text)

# #test case 3
# response = client.responses.create(
#     model="gpt-5-mini",
#     input="Explain machine learning in simple terms."
# )
# print(f"Response: {response.output_text}")
# print(f"Response ID: {response.id}")
# print(f"Tokens used: {response.usage.total_tokens}")
# print(f"Status: {response.status}")


# #test case 4: Controlling response generation
# response = openai_client.responses.create(
#     model="gpt-4.1",
#     instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
#     input="Write a creative story about AI.",
#     temperature=0.8,  # Higher temperature for more creativity
#     max_output_tokens=200  # Limit response length
# )
# print(response.output_text)