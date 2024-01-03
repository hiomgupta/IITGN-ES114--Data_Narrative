import pandas as pd


if __name__ == '__main__':

	df_aaup    = pd.read_csv('aaup.data', header=None)
	df_usnews  = pd.read_csv('usnews.data', header=None)

	print(df_aaup)
	print(df_usnews)
