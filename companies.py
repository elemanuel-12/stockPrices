urls = [
    'https://www.investing.com/equities/adidas-salomon',
    'https://www.investing.com/equities/coca-cola-co',
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/3m-co',
    'https://www.investing.com/equities/american-express',
    'https://www.investing.com/equities/amgen-inc',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/boeing-co',
    'https://www.investing.com/equities/cisco-sys-inc',
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/salesforce-com',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc',
    'https://www.investing.com/equities/wal-mart-stores',
    'https://www.investing.com/equities/disney',
    'https://www.investing.com/equities/twilio-inc-a',
    'https://www.investing.com/equities/tesla-motors',
    'https://www.investing.com/equities/gamestop-corp',
    'https://www.investing.com/equities/cemex-sab-de-cv-adr',
]

html_tags = {
    "company": ["h1", "class", 'mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr'],
    "price": ["div", "data-test", "instrument-price-last"],
    "change": ["span", "data-test", "instrument-price-change-percent"],
    "volume": ["dd", "data-test", "volume"],
    "year_change": ["dd", "data-test", "oneYearReturn"],
    "p_e_ratio": ["dd", "data-test", "ratio"],
    "eps": ["dd", "data-test", "eps"]
}