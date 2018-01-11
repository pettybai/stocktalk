from scripts import settings

# Query keys categorize tweets
# Each key or category corresponds to an array of keywords
queries = {'ETH': ['ETH', 'Ethereum'],
           'LTC': ['LTC', 'Litecoin'],
           'BTC': ['BTC', 'Bitcoin'],
           'XRP': ['XRP', 'Ripple'],
           'XLM': ['XLM', 'Stellar']}

# Aggregate volume and sentiment every 15 minutes
refresh = 15*60

streaming(settings.credentials, 
          queries, 
          refresh, 
          sentiment=True, 
          debug=True)