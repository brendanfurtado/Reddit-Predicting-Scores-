import json
import pandas as pd
pd.options.display.width = 0

with open("data.json") as fp:
    data = json.load(fp)

# popularity_score : a popularity score for this comment (based on the number of upvotes) (type: float)
# children : the number of replies to this comment (type: int)
# text : the text of this comment (type: string)
# controversiality : a score for how "controversial" this comment is (automatically computed by Reddit)
# is_root : if True, then this comment is a direct reply to a post; if False, this is a direct reply to another comment


class data_loading:

    dataframe = pd.DataFrame.from_dict(data, orient='columns')
