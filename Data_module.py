import pandas as pd
import numpy as np
import pickle
from keras.models import load_model
from collections import deque
import matplotlib.pyplot as plt

class Data_module:
    def __init__(self):
        pass

    def load_data(self):
        with open('./DataBase/CNS_predict_abnormal_accident_train_db_3D.bin', 'rb') as f: # 데이터 파일 변화시 수정 필요
            self.db = pickle.load(f)
        test_db = ['ab20-04_1.pkl', 'ab20-04_3.pkl', 'ab20-04_5.pkl', 'ab20-04_7.pkl', 'ab20-04_9.pkl', 'ab23-03-15.pkl',  'ab23-03-55.pkl',
               'ab59-02-1011.pkl', 'ab59-02-1021.pkl', 'ab59-02-1031.pkl', 'ab59-02-1041.pkl', 'ab60-02_101.pkl', 'ab60-02_103.pkl', 'ab60-02_105.pkl']
        print('전체 DataBase 구축 완료')
        return self.db, test_db # test_db의 return 목적 : 실행파일에서 활용할 예정임.

    def load_check_data(self, file_name):
        with open(f'./DataBase/CNS_db/pkl/{file_name}', 'rb') as f:
            check_db = pickle.load(f)
        self.check_db = check_db[30:-10] # test_db와 check_data의 shape을 일치하게 하기 위함. 추후에 데이터 shape 확인 필요함.
        print(f'{file_name}에 대한 Check_db 구축 완료')
        return self.check_db

    def compare_data_shape(self, file_name):
        if np.shape(self.db[file_name]['train_x_db'])[0] == np.shape(self.check_db)[0]:
            print('DB 및 Check_db의 Shape이 동일합니다.')
        else:
            print('Error : DB 및 Check_db의 Shape이 동일하지 않습니다. 다시 한번 확인해주세요!')

    def load_real_data(self, file_name, row): # 현재는 CNS와 연동이 되어있지 않아 임의로 실시간 데이터를 생성하는 목적으로 구성함.
        data = deque(maxlen=1)
        data.append(self.db[file_name]['train_x_db'][row])
        data = np.array(data)
        return data

    def load_real_check_data(self, row): # Check data는 Min-Max Scaler 사용 X
        check_data = deque(maxlen=1)
        check_parameter = deque(maxlen=1)
        check_data.append(self.check_db.iloc[row])
        check_parameter.append(self.check_db.iloc[row-2:row])
        check_data = pd.DataFrame(check_data)
        check_parameter = pd.DataFrame(check_parameter[0])
        return check_data, check_parameter


