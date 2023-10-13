import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

start_session = pd.Timestamp('2012-11-01')
end_session = pd.Timestamp('2022-11-01')

register(
    'SP-Datathon',
    csvdir_equities(
        ['daily'],
        './input/dt23-test',
    ),
    calendar_name='NYSE', # US equities
    start_session=start_session,
    end_session=end_session
)
