package constants

type RegexMatch struct {
	CryptoName string `json:"crypto"`
	RegexMatch string `json:"regexMatch"`
}

var (
	RegexMatches = []RegexMatch{
		{
			CryptoName: "btc",
			RegexMatch: "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
		},
		{
			CryptoName: "xmr",
			RegexMatch: "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}",
		},
		{
			CryptoName: "eth",
			RegexMatch: "^0x[a-fA-F0-9]{40}",
		},
		{
			CryptoName: "dash",
			RegexMatch: "^X[0-9A-HJ-NP-Za-km-z]{33}$",
		},
		{
			CryptoName: "doge",
			RegexMatch: "^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$",
		},
	}
)
