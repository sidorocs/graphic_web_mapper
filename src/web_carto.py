from page_analyzer import *
from utils import *
import argparse

def interface():
	parser = argparse.ArgumentParser(description="Extract links and forms from a given URL")
	parser.add_argument('-u', '--url', help="Base URL to extract links and forms from", required=True)
	parser.add_argument('-o', '--output', help="output file", required=True)
	parser.add_argument('-e', '--extension', help="file format (txt or json)", choices=['txt', 'json'], required=True)

	args = parser.parse_args()
	
	base_url = args.url
	output_file = args.output
	file_extension = args.extension
	# if file_extension not in ['txt', 'json']:
	#	print(f"Error : Format {file_extension} non pris en charge.")
	
	extracted_data = map_website(base_url, DONT_CRAWL_THAT) 
	if file_extension == 'txt':
		write_dict_to_txt(extracted_data, output_file)
	if file_extension == 'json':
		write_dict_to_json(extracted_data, output_file)

	print("Done ...")



if __name__ == "__main__":
    interface()

	



    	
    	
