from src.available_bonds import main
from utils.extract_from_sheets import get_bonos_purchased

df = get_bonos_purchased()

print(df.columns)
