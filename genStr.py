try:
    from pyrogram import Client
except Exception as error:
       print(error)
       exit(1)

name      = "DarkPyro"
api_id    = 50322
api_hash  = "9ff1a639196c0779c86dd661af8522ba"

with Client(name=name,
            api_id=api_id,
            api_hash=api_hash,
            in_memory=True) as babu:
     String = babu.export_session_string()
     print(
     f"""

     {String}

     """
     )
