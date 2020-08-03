from utils import create_input

if __name__ == '__main__':
	# Create input files (along with word map)
	create_input(dataset='coco',
				 karpathy_json_path='../datasets/coco/splits/dataset_coco.json',
				 image_folder='../datasets/coco/images/',
				 captions_per_image=5,
				 min_word_freq=5,
				 output_folder='../saved_inputs/',
				 max_len=50)