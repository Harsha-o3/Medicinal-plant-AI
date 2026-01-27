"""
plant_info.py

A mapping of plant/common names (matching the `dataset/` folders) to a small
metadata dictionary. Fields are intentionally minimal so the file can be
extended later from authoritative sources.

Helper functions are provided to access the mapping programmatically.
"""

from typing import Dict, List, Optional

plant_info: Dict[str, Dict[str, object]] = {
    "Ajwain": {
        "scientific_name": "Trachyspermum ammi",
        "family": "Apiaceae",
        "origin": "Middle East/India",
        "compounds": "Thymol, carvacrol",
        "pharmacological_properties": "Carminative, mild antimicrobial",
        "traditional_uses": "Digestive aid, relieves flatulence and indigestion",
        "precautions": "Use in culinary amounts; avoid large medicinal doses during pregnancy without medical advice",
    },
    "Alocasia plant": {
        "scientific_name": "Alocasia spp.",
        "family": "Araceae",
        "origin": "Tropical Asia",
        "compounds": "Calcium oxalates (irritant crystals)",
        "pharmacological_properties": "Not well characterized; raw plant may be irritating",
        "traditional_uses": "Primarily ornamental; some species used in folk medicine after processing",
        "precautions": "Contains irritant crystals — toxic if chewed raw",
    },
    "Aloe Plant": {
        "scientific_name": "Aloe barbadensis Miller",
        "family": "Asphodelaceae",
        "origin": "Arabian Peninsula",
        "compounds": "Aloin, acemannan, various polysaccharides",
        "pharmacological_properties": "Topical soothing, wound-supporting properties (traditional)",
        "traditional_uses": "Topical for minor skin irritations and burns",
        "precautions": "Use topical products as directed; oral aloe preparations can have laxative effects and should be used cautiously",
    },
    "Amapalya": {
        "scientific_name": "Unknown",
        "family": "Unknown",
        "origin": "Unknown",
        "compounds": "Not available",
        "pharmacological_properties": "Not available",
        "traditional_uses": "Not available",
        "precautions": "Information not available",
    },
    "Angelica": {
        "scientific_name": "Angelica archangelica",
        "family": "Apiaceae",
        "origin": "Europe and Asia",
        "compounds": "Furanocoumarins, essential oils",
        "pharmacological_properties": "Carminative, aromatic; some digestive support (traditional)",
        "traditional_uses": "Digestive aid, mild expectorant",
        "precautions": "May increase photosensitivity in some individuals due to furanocoumarins",
    },
    "Barberry": {
        "scientific_name": "Berberis vulgaris",
        "family": "Berberidaceae",
        "origin": "Europe",
        "compounds": "Berberine and related alkaloids",
        "pharmacological_properties": "Traditionally considered antimicrobial and digestive support",
        "traditional_uses": "Used in traditional systems for digestion and mild infections",
        "precautions": "Avoid high doses during pregnancy; consult a professional for medicinal use",
    },
    "Basil": {
        "scientific_name": "Ocimum basilicum",
        "family": "Lamiaceae",
        "origin": "Central Africa/Asia",
        "compounds": "Eugenol, linalool, methyl chavicol (varies by variety)",
        "pharmacological_properties": "Aromatic, mild anti-inflammatory properties (traditional)",
        "traditional_uses": "Culinary herb; used in folk medicine for digestive and mild calming purposes",
        "precautions": "Generally safe in food amounts; concentrated essential oils should be used with care",
    },
    "Beechh Tree": {
        "scientific_name": "Fagus spp.",
        "family": "Fagaceae",
        "origin": "Temperate Europe/Asia/North America",
        "compounds": "Not available",
        "pharmacological_properties": "Not well documented",
        "traditional_uses": "Some traditional uses of bark or leaves in folk remedies",
        "precautions": "Information limited; avoid assuming medicinal safety",
    },
    "Belladonna": {
        "scientific_name": "Atropa belladonna",
        "family": "Solanaceae",
        "origin": "Europe/North Africa/Western Asia",
        "compounds": "Tropane alkaloids (atropine, scopolamine)",
        "pharmacological_properties": "Powerful anticholinergic effects; historically used medicinally but toxic",
        "traditional_uses": "Historically used in small, controlled doses for various conditions (very toxic)",
        "precautions": "Highly toxic — do not use without professional supervision",
    },
    "Betel leaf": {
        "scientific_name": "Piper betle",
        "family": "Piperaceae",
        "origin": "Southeast Asia",
        "compounds": "Eugenol and other phenylpropanoids",
        "pharmacological_properties": "Aromatic, traditional antimicrobial properties",
        "traditional_uses": "Chewed culturally; used in traditional remedies for oral hygiene and digestion",
        "precautions": "Chewing with tobacco or areca nut has known health risks",
    },
    "Black walnuts": {
        "scientific_name": "Juglans nigra",
        "family": "Juglandaceae",
        "origin": "North America",
        "compounds": "Juglone (in some parts), tannins",
        "pharmacological_properties": "Historically used in folk remedies; limited modern evidence",
        "traditional_uses": "Topical/folk uses; caution with ingestion",
        "precautions": "May cause allergic reactions in sensitive individuals",
    },
    "Brahmi": {
        "scientific_name": "Bacopa monnieri",
        "family": "Plantaginaceae",
        "origin": "India",
        "compounds": "Bacosides and other saponins",
        "pharmacological_properties": "Traditionally used for cognitive support",
        "traditional_uses": "Used in Ayurvedic medicine for memory and nervous system support",
        "precautions": "Use as traditionally directed; consult practitioner for therapeutic dosing",
    },
    "California": {
        "scientific_name": "Unknown",
        "family": "Unknown",
        "origin": "Unknown",
        "compounds": "Not available",
        "pharmacological_properties": "Not available",
        "traditional_uses": "Not available",
        "precautions": "Information not available",
    },
    "Coriander": {
        "scientific_name": "Coriandrum sativum",
        "family": "Apiaceae",
        "origin": "Southern Europe/Northern Africa/Western Asia",
        "compounds": "Linalool, coriandrol (in essential oil)",
        "pharmacological_properties": "Aromatic, digestive-supporting (traditional)",
        "traditional_uses": "Culinary use; used for mild digestive complaints",
        "precautions": "Generally safe in food amounts; concentrated extracts use with caution",
    },
    "Corn flower": {
        "scientific_name": "Centaurea cyanus",
        "family": "Asteraceae",
        "origin": "Europe",
        "compounds": "Anthocyanins and flavonoids",
        "pharmacological_properties": "Mild astringent and soothing properties (traditional)",
        "traditional_uses": "Used in herbal infusions for mild eye and skin soothing",
        "precautions": "Avoid concentrated use without guidance",
    },
    "Curry leaves": {
        "scientific_name": "Murraya koenigii",
        "family": "Rutaceae",
        "origin": "India",
        "compounds": "Carbazole alkaloids, essential oils",
        "pharmacological_properties": "Aromatic; used traditionally to support digestion",
        "traditional_uses": "Culinary and traditional digestive support",
        "precautions": "Generally safe in food amounts",
    },
    "Fewer few": {
        "scientific_name": "Unknown",
        "family": "Unknown",
        "origin": "Unknown",
        "compounds": "Not available",
        "pharmacological_properties": "Not available",
        "traditional_uses": "Not available",
        "precautions": "Information not available",
    },
    "Veronica": {
        "scientific_name": "Veronica spp.",
        "family": "Plantaginaceae",
        "origin": "Temperate regions",
        "compounds": "Not well characterized",
        "pharmacological_properties": "Limited data",
        "traditional_uses": "Some species used in folk medicine",
        "precautions": "Information limited; use caution",
    },
    "Garlic": {
        "scientific_name": "Allium sativum",
        "family": "Amaryllidaceae",
        "origin": "Central Asia",
        "compounds": "Allicin and sulfur-containing compounds",
        "pharmacological_properties": "Traditionally antimicrobial and cardiovascular-supporting",
        "traditional_uses": "Culinary and traditional use for circulation and infection support",
        "precautions": "Can interact with anticoagulant medications; avoid high-dose supplements without advice",
    },
    "Gingko": {
        "scientific_name": "Ginkgo biloba",
        "family": "Ginkgoaceae",
        "origin": "China",
        "compounds": "Ginkgolides, bilobalide, flavonoids",
        "pharmacological_properties": "Traditionally used for circulation and cognitive support",
        "traditional_uses": "Used in traditional and modern herbal preparations for cognition and circulation",
        "precautions": "May interact with blood-thinning medications; consult a professional",
    },
    "Golden panthos": {
        "scientific_name": "Unknown",
        "family": "Unknown",
        "origin": "Unknown",
        "compounds": "Not available",
        "pharmacological_properties": "Not available",
        "traditional_uses": "Not available",
        "precautions": "Information not available",
    },
    "Hibiscus leaves": {
        "scientific_name": "Hibiscus spp.",
        "family": "Malvaceae",
        "origin": "Tropical and subtropical regions",
        "compounds": "Anthocyanins, flavonoids",
        "pharmacological_properties": "Antioxidant properties (traditional)",
        "traditional_uses": "Used in infusions for cardiovascular and cooling effects",
        "precautions": "Generally safe in food amounts; check interactions for specific supplements",
    },
    "Horse Chestnuts": {
        "scientific_name": "Aesculus hippocastanum",
        "family": "Sapindaceae",
        "origin": "Southeastern Europe",
        "compounds": "Aescin and triterpenoid saponins",
        "pharmacological_properties": "Traditionally used for venous circulation support",
        "traditional_uses": "Topical and oral traditional uses for venous insufficiency (processed extracts)",
        "precautions": "Do not ingest raw seeds; use standardized preparations and consult a professional",
    },
    "Horse tail": {
        "scientific_name": "Equisetum arvense",
        "family": "Equisetaceae",
        "origin": "Cosmopolitan temperate regions",
        "compounds": "Silica, flavonoids",
        "pharmacological_properties": "Traditional diuretic and mineral-supporting uses",
        "traditional_uses": "Used in folk medicine for urinary and wound applications",
        "precautions": "Long-term use not recommended without guidance; contains compounds that may be harmful in excess",
    },
    "Indian beech": {
        "scientific_name": "Pongamia pinnata",
        "family": "Fabaceae",
        "origin": "Indian subcontinent",
        "compounds": "Fatty acids and flavonoids (in seeds/oil)",
        "pharmacological_properties": "Traditional uses in topical preparations",
        "traditional_uses": "Used in traditional medicine and as a source of oil",
        "precautions": "Processing often required; avoid ingestion of unprocessed seed materials",
    },
    "Jack Fruit Leaves": {
        "scientific_name": "Artocarpus heterophyllus",
        "family": "Moraceae",
        "origin": "South Asia",
        "compounds": "Various phytochemicals in leaves and fruit",
        "pharmacological_properties": "Limited traditional claims",
        "traditional_uses": "Leaves used in some folk remedies",
        "precautions": "Information limited; use caution",
    },
    "Jade tail": {
        "scientific_name": "Unknown",
        "family": "Unknown",
        "origin": "Unknown",
        "compounds": "Not available",
        "pharmacological_properties": "Not available",
        "traditional_uses": "Not available",
        "precautions": "Information not available",
    },
    "Lavender": {
        "scientific_name": "Lavandula angustifolia",
        "family": "Lamiaceae",
        "origin": "Mediterranean",
        "compounds": "Linalool, linalyl acetate",
        "pharmacological_properties": "Aromatic calming effects (traditional)",
        "traditional_uses": "Aromatherapy for relaxation and sleep support",
        "precautions": "Use essential oils diluted; avoid ingestion of undiluted oils",
    },
    "Liquirice root": {
        "scientific_name": "Glycyrrhiza glabra",
        "family": "Fabaceae",
        "origin": "Southern Europe/Western Asia",
        "compounds": "Glycyrrhizin and saponins",
        "pharmacological_properties": "Soothing demulcent and anti-inflammatory (traditional)",
        "traditional_uses": "Used for sore throats and digestive soothing",
        "precautions": "Large doses can affect blood pressure and potassium levels; avoid prolonged high-dose use",
    },
    "Malunggay": {
        "scientific_name": "Moringa oleifera",
        "family": "Moringaceae",
        "origin": "Indian subcontinent",
        "compounds": "Vitamins, antioxidants, various phytochemicals",
        "pharmacological_properties": "Nutrient-rich; antioxidant properties (traditional)",
        "traditional_uses": "Used as a nutrient-dense food and in traditional medicine",
        "precautions": "Generally safe as food; consult before using concentrated extracts",
    },
    "Mint": {
        "scientific_name": "Mentha spp.",
        "family": "Lamiaceae",
        "origin": "Europe/Asia",
        "compounds": "Menthol, menthone, various essential oil components",
        "pharmacological_properties": "Digestive-aiding aromatic properties (traditional)",
        "traditional_uses": "Used for digestive comfort and aromatic purposes",
        "precautions": "Avoid concentrated peppermint oil in infants; use with care",
    },
    "Mother wort": {
        "scientific_name": "Leonurus cardiaca",
        "family": "Lamiaceae",
        "origin": "Europe/Asia",
        "compounds": "Iridoids and alkaloids (varies)",
        "pharmacological_properties": "Traditionally used as a cardiac tonic in folk medicine",
        "traditional_uses": "Used historically for heart-related folk uses",
        "precautions": "Consult a professional before use, particularly with heart medications",
    },
    "Neem": {
        "scientific_name": "Azadirachta indica",
        "family": "Meliaceae",
        "origin": "Indian subcontinent",
        "compounds": "Azadirachtin and limonoids",
        "pharmacological_properties": "Traditionally antimicrobial and insect-repellent",
        "traditional_uses": "Topical uses for skin and hygiene in traditional systems",
        "precautions": "Avoid large internal doses; consult before medicinal use",
    },
    "Papaya": {
        "scientific_name": "Carica papaya",
        "family": "Caricaceae",
        "origin": "Tropical Americas",
        "compounds": "Papain and proteolytic enzymes",
        "pharmacological_properties": "Digestive enzyme activity (traditional)",
        "traditional_uses": "Used to aid digestion and tenderize meat",
        "precautions": "Unripe papaya may have different effects; consult in pregnancy",
    },
    "Periwinkle": {
        "scientific_name": "Catharanthus roseus",
        "family": "Apocynaceae",
        "origin": "Madagascar",
        "compounds": "Vinca alkaloids (important pharmaceutical derivatives)",
        "pharmacological_properties": "Contains compounds that have been used as pharmaceuticals (cancer drugs derived from alkaloids)",
        "traditional_uses": "Used in traditional medicine; some compounds led to important drugs",
        "precautions": "Do not self-medicate; contains potent alkaloids",
    },
    "Ponytail palm palm": {
        "scientific_name": "Beaucarnea recurvata",
        "family": "Asparagaceae",
        "origin": "Mexico",
        "compounds": "Not available",
        "pharmacological_properties": "Primarily ornamental",
        "traditional_uses": "Ornamental plant",
        "precautions": "Not used medicinally",
    },
    "Queen  annes  lace": {
        "scientific_name": "Daucus carota",
        "family": "Apiaceae",
        "origin": "Europe/Asia",
        "compounds": "Carotenoids and essential oils (wild carrot)",
        "pharmacological_properties": "Historically edible/medicinal uses in folk medicine",
        "traditional_uses": "Wild carrot used historically as food and folk remedy",
        "precautions": "Can be confused with toxic Apiaceae species; care required",
    },
    "Rauwolfia": {
        "scientific_name": "Rauvolfia serpentina",
        "family": "Apocynaceae",
        "origin": "Indian subcontinent",
        "compounds": "Reserpine and other indole alkaloids",
        "pharmacological_properties": "Historically used for blood pressure and agitation (potent pharmacology)",
        "traditional_uses": "Used in traditional medicine for hypertension-related uses",
        "precautions": "Contains potent alkaloids — not for unsupervised use",
    },
    "Rosemary": {
        "scientific_name": "Salvia rosmarinus",
        "family": "Lamiaceae",
        "origin": "Mediterranean",
        "compounds": "Carnosic acid, rosmarinic acid, essential oils",
        "pharmacological_properties": "Aromatic antioxidant properties (traditional)",
        "traditional_uses": "Culinary and traditional aromatic uses",
        "precautions": "Generally safe in culinary amounts; concentrated extracts with care",
    },
    "Rubber plant": {
        "scientific_name": "Ficus elastica",
        "family": "Moraceae",
        "origin": "Southeast Asia",
        "compounds": "Latex compounds and ficin (in some Ficus)",
        "pharmacological_properties": "Primarily ornamental; limited medicinal use",
        "traditional_uses": "Some folk uses of Ficus species",
        "precautions": "Latex can cause contact dermatitis in sensitive people",
    },
    "Senna": {
        "scientific_name": "Senna alexandrina",
        "family": "Fabaceae",
        "origin": "Northern Africa/Asia",
        "compounds": "Anthraquinone glycosides (sennosides)",
        "pharmacological_properties": "Stimulant laxative properties (well known)",
        "traditional_uses": "Used as a laxative in traditional systems",
        "precautions": "Should not be used long-term without supervision; can cause cramping and electrolyte changes",
    },
    "Slippery Elm": {
        "scientific_name": "Ulmus rubra",
        "family": "Ulmaceae",
        "origin": "North America",
        "compounds": "Mucilaginous polysaccharides",
        "pharmacological_properties": "Demulcent, soothing to mucous membranes (traditional)",
        "traditional_uses": "Used as a soothing preparation for throat and digestive discomfort",
        "precautions": "Generally used topically or as lozenges; avoid contaminated sources",
    },
    "Snake plant": {
        "scientific_name": "Sansevieria trifasciata",
        "family": "Asparagaceae",
        "origin": "West Africa",
        "compounds": "Not well characterized for medicinal compounds",
        "pharmacological_properties": "Primarily ornamental",
        "traditional_uses": "Ornamental; some folk uses reported",
        "precautions": "May be mildly toxic if ingested by pets",
    },
    "Swiss plant": {
        "scientific_name": "Unknown",
        "family": "Unknown",
        "origin": "Unknown",
        "compounds": "Not available",
        "pharmacological_properties": "Not available",
        "traditional_uses": "Not available",
        "precautions": "Information not available",
    },
    "Tea leaves": {
        "scientific_name": "Camellia sinensis",
        "family": "Theaceae",
        "origin": "East Asia",
        "compounds": "Caffeine, catechins (EGCG), theanine",
        "pharmacological_properties": "Stimulant and antioxidant properties (traditional)",
        "traditional_uses": "Beverage and traditional tonic",
        "precautions": "Caffeine content may affect sensitive individuals",
    },
    "Terminalia leavees": {
        "scientific_name": "Terminalia spp.",
        "family": "Combretaceae",
        "origin": "Tropical regions",
        "compounds": "Tannins and polyphenols (varies by species)",
        "pharmacological_properties": "Traditionally used for digestive and tonic purposes",
        "traditional_uses": "Used in traditional preparations in some cultures",
        "precautions": "Species-specific — consult reliable sources",
    },
    "Thyme": {
        "scientific_name": "Thymus vulgaris",
        "family": "Lamiaceae",
        "origin": "Mediterranean",
        "compounds": "Thymol, carvacrol, essential oils",
        "pharmacological_properties": "Antimicrobial and aromatic properties (traditional)",
        "traditional_uses": "Culinary and traditional respiratory support",
        "precautions": "Concentrated oils should be used with care",
    },
    "Turmeric leaves": {
        "scientific_name": "Curcuma longa",
        "family": "Zingiberaceae",
        "origin": "South Asia",
        "compounds": "Curcuminoids (e.g., curcumin)",
        "pharmacological_properties": "Anti-inflammatory and antioxidant properties (traditional)",
        "traditional_uses": "Used in culinary and traditional preparations",
        "precautions": "High-dose extracts should be used under guidance",
    },
    "Veronica": {
        "scientific_name": "Veronicastrum/Veronica spp.",
        "family": "Plantaginaceae",
        "origin": "Temperate regions",
        "compounds": "Not well characterized",
        "pharmacological_properties": "Limited data",
        "traditional_uses": "Some species used in folk remedies",
        "precautions": "Information limited; use caution",
    },
    "Winter Green": {
        "scientific_name": "Gaultheria procumbens",
        "family": "Ericaceae",
        "origin": "North America",
        "compounds": "Methyl salicylate (in essential oil)",
        "pharmacological_properties": "Topical analgesic properties (traditional)",
        "traditional_uses": "Topical use for mild muscle aches in traditional preparations",
        "precautions": "Oil is potent and should be diluted; avoid in people allergic to salicylates",
    },
    "yellow dock": {
        "scientific_name": "Rumex crispus",
        "family": "Polygonaceae",
        "origin": "Europe/Asia",
        "compounds": "Anthraquinones (in some species), tannins",
        "pharmacological_properties": "Mild laxative and tonic properties (traditional)",
        "traditional_uses": "Used as a mild laxative and for mineral tonics in folk medicine",
        "precautions": "Avoid excessive use; check for interactions",
    },
}


def list_plants() -> List[str]:
    """Return a sorted list of plant names available in the mapping."""
    return sorted(plant_info.keys(), key=lambda s: s.lower())


def get_info(name: str) -> Optional[Dict[str, object]]:
    """Retrieve metadata for a plant by name.

    Performs a case-insensitive lookup. Returns None if not found.
    """
    # exact match
    if name in plant_info:
        return plant_info[name]

    # case-insensitive search
    lower = name.lower()
    for key in plant_info:
        if key.lower() == lower:
            return plant_info[key]

    return None


def search_by_keyword(keyword: str) -> List[str]:
    """Return plant names where the keyword appears in any metadata field."""
    k = keyword.lower()
    matches: List[str] = []
    for name, info in plant_info.items():
        if k in name.lower():
            matches.append(name)
            continue
        # check simple string fields
        for v in (info.get("scientific_name"), info.get("family"), info.get("origin")):
            if isinstance(v, str) and k in v.lower():
                matches.append(name)
                break
        else:
            # check uses list
            uses = info.get("uses", [])
            if any(k in (u or "").lower() for u in uses if isinstance(u, str)):
                matches.append(name)

    return matches


if __name__ == "__main__":
    # Quick sanity checks so this module can be run directly.
    print(f"Total plants: {len(plant_info)}")
    # show first 10 plants
    for p in list_plants()[:10]:
        print(p)
