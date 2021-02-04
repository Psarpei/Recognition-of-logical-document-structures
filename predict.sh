FILE=PLACE_YOUR_FILES_HERE/$1
python3 graminput_to_text.py $FILE.txt
python3 text_to_network_input.py $FILE.txt
python get_oracle.py train_set_add_t.txt ${FILE}_graminput.txt > $FILE.oracle
build/nt-parser/nt-parser --cnn-mem 2500 -x -T train.oracle -p $FILE.oracle -C ${FILE}_graminput.txt -P --lstm_input_dim 128 --hidden_dim 128 -m ntparse_pos_0_2_32_128_16_128-pid7064.params > ${FILE}_predict.txt
python3 evaluation.py $FILE
python3 prediction_to_XML.py $FILE