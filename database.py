import os
from dotenv import load_dotenv

load_dotenv()

from supabase import create_client

uri = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(uri, key)

def AddNewRecepie(naziv_recepta,sol,papar,ljuta_paprika,slatka_paprika,bijeli_luk):
    supabase.table("recepti").insert({"naziv_recepta": naziv_recepta, "sol": sol, "papar": papar, "ljuta_paprika": ljuta_paprika, "slatka_paprika": slatka_paprika, "bijeli_luk":bijeli_luk}).execute()

