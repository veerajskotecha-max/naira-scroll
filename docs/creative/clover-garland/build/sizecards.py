# Size-guide cards for the two pieces listed on 30 Oct 2026, in the house formats (../../size-cards/build/cards.py):
#   Clover Garland Bracelet: the bracelet ruler card, adjustable 17-21 cm (about 17 cm to the clasp, plus the extender);
#   Rivière Classique Necklace: the neck-outline card at 40 cm.
# Both lengths are estimates from the owner's photos (README), so each card says the length is approximate.
# Usage: python3 -I sizecards.py -> ../shopify/clover-garland-bracelet-size-guide.jpg and
#        ../../tennis-necklace/shopify/riviere-classique-necklace-size-guide.jpg
import importlib.util, os
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location("cards", os.path.join(H, "../../size-cards/build/cards.py"))
C = importlib.util.module_from_spec(s); s.loader.exec_module(C)
C.SGB.card("Clover Garland Bracelet", 17, (17, 21), "Length is approximate.").save(
    os.path.join(H, "../shopify/clover-garland-bracelet-size-guide.jpg"), quality=92)
C.necklace("Rivière Classique Necklace", [40], "40 cm · stones 3 mm", "Chain length is approximate.").save(
    os.path.join(H, "../../tennis-necklace/shopify/riviere-classique-necklace-size-guide.jpg"), quality=92)
print("cards drawn")
