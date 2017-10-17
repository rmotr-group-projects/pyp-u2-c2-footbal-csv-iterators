from football_explorer import FootballExplorer


explorer = FootballExplorer(csv_file_name='test_data.csv')
results = explorer.search(country = "Argentina")
iterator = iter(results)

player = next(iterator)
print(player)
player = next(iterator)
print(player)
player = next(iterator)
print(player)
