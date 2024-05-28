from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()


client = SecretClient(vault_url='https://key_vault_url.azure.net/', credential=credential)

jdbcPassword = client.get_secret('name_of_key_vault_password')

jdbcUsername = "username"
jdbcPassword = jdbcPassword.value