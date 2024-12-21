import os
import random

def split_dataset(file_path_en, file_path_vi, train_path_en, train_path_vi, val_path_en, val_path_vi, test_path_en, test_path_vi, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, seed=42):
    """
    Split English and Vietnamese datasets into train, validation, and test sets.

    :param file_path_en: Path to the English dataset.
    :param file_path_vi: Path to the Vietnamese dataset.
    :param train_path_en: Path to save the English training set.
    :param train_path_vi: Path to save the Vietnamese training set.
    :param val_path_en: Path to save the English validation set.
    :param val_path_vi: Path to save the Vietnamese validation set.
    :param test_path_en: Path to save the English test set.
    :param test_path_vi: Path to save the Vietnamese test set.
    :param train_ratio: Proportion of the dataset to include in the training split.
    :param val_ratio: Proportion of the dataset to include in the validation split.
    :param test_ratio: Proportion of the dataset to include in the test split.
    :param seed: Random seed for reproducibility.
    """
    # Đảm bảo tính ngẫu nhiên có thể tái lập
    random.seed(seed)

    # Đọc dữ liệu từ file
    with open(file_path_en, 'r', encoding='utf-8') as infile_en, open(file_path_vi, 'r', encoding='utf-8') as infile_vi:
        lines_en = infile_en.readlines()
        lines_vi = infile_vi.readlines()

    # Kiểm tra tính đồng bộ của hai file
    if len(lines_en) != len(lines_vi):
        raise ValueError("The English and Vietnamese files must have the same number of lines.")

    # Shuffle dữ liệu
    combined = list(zip(lines_en, lines_vi))
    random.shuffle(combined)
    lines_en, lines_vi = zip(*combined)

    # Tính toán số lượng mẫu cho từng tập
    total_lines = len(lines_en)
    train_size = int(total_lines * train_ratio)
    val_size = int(total_lines * val_ratio)

    # Chia dữ liệu
    train_data_en = lines_en[:train_size]
    train_data_vi = lines_vi[:train_size]
    val_data_en = lines_en[train_size:train_size + val_size]
    val_data_vi = lines_vi[train_size:train_size + val_size]
    test_data_en = lines_en[train_size + val_size:]
    test_data_vi = lines_vi[train_size + val_size:]

    # Ghi dữ liệu vào file
    with open(train_path_en, 'w', encoding='utf-8') as train_file_en, \
         open(train_path_vi, 'w', encoding='utf-8') as train_file_vi, \
         open(val_path_en, 'w', encoding='utf-8') as val_file_en, \
         open(val_path_vi, 'w', encoding='utf-8') as val_file_vi, \
         open(test_path_en, 'w', encoding='utf-8') as test_file_en, \
         open(test_path_vi, 'w', encoding='utf-8') as test_file_vi:
        train_file_en.writelines(train_data_en)
        train_file_vi.writelines(train_data_vi)
        val_file_en.writelines(val_data_en)
        val_file_vi.writelines(val_data_vi)
        test_file_en.writelines(test_data_en)
        test_file_vi.writelines(test_data_vi)

    print(f"Dataset split completed:\n- Train set: {len(train_data_en)} samples saved to {train_path_en} and {train_path_vi}\n- Validation set: {len(val_data_en)} samples saved to {val_path_en} and {val_path_vi}\n- Test set: {len(test_data_en)} samples saved to {test_path_en} and {test_path_vi}")

# File paths
input_file_en = 'data/clean_en.txt'
input_file_vi = 'data/clean_vi.txt'
train_file_en = 'data/train_en.txt'
train_file_vi = 'data/train_vi.txt'
val_file_en = 'data/val_en.txt'
val_file_vi = 'data/val_vi.txt'
test_file_en = 'data/test_en.txt'
test_file_vi = 'data/test_vi.txt'

# Split the dataset
split_dataset(input_file_en, input_file_vi, train_file_en, train_file_vi, val_file_en, val_file_vi, test_file_en, test_file_vi, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, seed=42)
