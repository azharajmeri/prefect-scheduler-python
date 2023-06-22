"""
SECRET BLOCK
------------
The secret block in Prefect enables you to securely store sensitive values such as keys
and tokens that are needed at various stages of your workflow.
"""
from prefect.blocks.system import Secret

secret_block = Secret.load("secret_test")

# Access the stored secret
print(secret_block.get())
