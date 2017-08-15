from __future__ import unicode_literals

import pytest
from football_explorer import FootballExplorer


def test_cant_search_without_params():
    explorer = FootballExplorer(csv_file_name='test_data.csv')
    with pytest.raises(ValueError):
        next(explorer.search())


def test_explorer_returns_all():
    explorer = FootballExplorer(csv_file_name='test_data.csv')
    results = explorer.all()
    iterator = iter(results)

    # 1st player
    player = next(iterator)
    assert player.number == '1'
    assert player.name == 'Juan Botasso'
    assert player.country == 'Argentina'

    # Fast-forward 12 players
    for _ in range(12):
        next(iterator)

    # Last player
    player = next(iterator)
    assert player.number == '-'
    assert player.name == 'Kim Shin-Wook'
    assert player.country == 'South Korea'

    with pytest.raises(StopIteration):
        next(iterator)


def test_search_by_country():
    explorer = FootballExplorer(csv_file_name='test_data.csv')
    results = explorer.search(country='Argentina')
    iterator = iter(results)
    # 1st player
    player = next(iterator)
    assert player.number == '1'
    assert player.name == 'Juan Botasso'
    assert player.country == 'Argentina'

    # 2nd player
    player = next(iterator)
    assert player.number == '9'
    assert player.name == 'Roberto Cherro'
    assert player.country == 'Argentina'
    
    with pytest.raises(StopIteration):
        next(iterator)


def test_search_by_country_and_year():
    explorer = FootballExplorer(csv_file_name='test_data.csv')
    results = explorer.search(country='Brazil', year=2010)
    iterator = iter(results)
    # 1st player
    player = next(iterator)
    assert player.name == 'Oscar'
    assert player.country == 'Brazil'

    # 2nd player
    player = next(iterator)
    assert player.name == 'Paulinho'
    assert player.country == 'Brazil'
    print(results)
    with pytest.raises(StopIteration):
        next(iterator)
