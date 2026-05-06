from modules.alliance.party_sync import load_alliance


class AllianceWidget:

    def get_counts(self):
        data = load_alliance()

        return {
            "A": len(data["alliance_a"]["members"]),
            "B": len(data["alliance_b"]["members"]),
            "C": len(data["alliance_c"]["members"])
        }