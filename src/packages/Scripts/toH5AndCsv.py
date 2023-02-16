from payloadHex import payloadHexParser
from payloadWise import payloadWiseParser
from payloadKs import payloadKSParser
import h5py
import numpy as np
from datetime import datetime


def WiseToNumpy():
    payloadWise = payloadWiseParser()
    x_matrix = []
    y_matrix = []
    z_matrix = []
    time_matrix = []
    for item in payloadWise:
            payload = item.get("payload")
            time = item.get("time")
            # se tiver Accelerometer
            if "Accelerometer" in payload:
                acc = payload["Accelerometer"]
                x = acc["X-Axis"]
                y = acc["Y-Axis"]
                z = acc["Z-Axis"]

                x_matrix.append([x['OAVelocity'], x['Peakmg'], x['RMSmg'], x['Kurtosis'], x['CrestFactor'], x['Skewness'], x['Deviation'], x['Peak-to-Peak Displacement']])
                y_matrix.append([y['OAVelocity'], y['Peakmg'], y['RMSmg'], y['Kurtosis'], y['CrestFactor'], y['Skewness'], y['Deviation'], y['Peak-to-Peak Displacement']])
                z_matrix.append([z['OAVelocity'], z['Peakmg'], z['RMSmg'], z['Kurtosis'], z['CrestFactor'], z['Skewness'], z['Deviation'], z['Peak-to-Peak Displacement']])
                dt = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                time_matrix.append(dt)


    x_matrix = np.array(x_matrix)
    y_matrix = np.array(y_matrix)
    z_matrix = np.array(z_matrix)
    time_matrix = np.array(time_matrix, dtype='datetime64[ns]')
    time_matrix = time_matrix.astype('int64')
    return x_matrix, y_matrix, z_matrix, time_matrix

def WiseToH5():
    x_matrix, y_matrix, z_matrix, time_matrix = WiseToNumpy()
    with h5py.File("./saida/wise/payloadWise.h5", "w") as f:
        f.create_dataset("x", data=x_matrix)
        f.create_dataset("y", data=y_matrix)
        f.create_dataset("z", data=z_matrix)
        f.create_dataset("time", data=time_matrix)

def WiseToCsv():
    x_matrix, y_matrix, z_matrix, time_matrix = WiseToNumpy()
    output_matrix = np.concatenate((x_matrix, y_matrix, z_matrix), axis=1)
    # criar um csv pra cada
    np.savetxt("./saida/wise/payloadWise.csv", output_matrix, delimiter=",")
    np.savetxt("./saida/wise/time.csv", time_matrix, delimiter=",")



def HexToNumpy():
    # {"InletPressure": 16.93051528930664, "OutletPressure": 1011.0496215820312, "OutletTemperature": 83.23367309570312, "InverterSpeed": 4558.0}', 'timestamp': '2023-02-16 02:30:36'}
    output = []
    time_matrix = []
    for item in payloadHexParser():
        payload = item.get("payload")
        time = item.get("time")
        # se tiver Accelerometer
        if "InletPressure" in payload:
            inletPressure = payload["InletPressure"]
            outletPressure = payload["OutletPressure"]
            outletTemperature = payload["OutletTemperature"]
            inverterSpeed = payload["InverterSpeed"]
            
            output.append([inletPressure, outletPressure, outletTemperature, inverterSpeed])
            
            dt = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            time_matrix.append(dt)


    output_matrix = np.array(output)
    time_matrix = np.array(time_matrix, dtype='datetime64[ns]')
    time_matrix = time_matrix.astype('int64')


    return output_matrix , time_matrix

def HexToH5():
    output_matrix , time_matrix = HexToNumpy()
    with h5py.File("./saida/hex/payloadHex.h5", "w") as f:
        f.create_dataset("payload", data=output_matrix)
        f.create_dataset("time", data=time_matrix)

def HexToCsv():
    output_matrix , time_matrix = HexToNumpy()
    # criar um csv pra cada
    np.savetxt("./saida/hex/payloadHex.csv", output_matrix, delimiter=",")
    np.savetxt("./saida/hex/time.csv", time_matrix, delimiter=",")
    
    
def KSToNumpy():
    # {"n": "temperature", "u": "Cel", "v": 52.0}, {"n": "frequency", "u": "Hz", "v": 60.0}, {"n": "phaseA_voltage", "u": "V", "v": 221.5}, {"n": "phaseA_current", "u": "A", "v": 3.5}, {"n": "phaseA_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseA_active", "u": "J", "v": 1362168000.0}, {"n": "phaseA_reactive", "u": "J", "v": 195624000.0}, {"n": "phaseA_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "phaseB_voltage", "u": "V", "v": 221.09999999999999}, {"n": "phaseB_current", "u": "A", "v": 3.6000000000000001}, {"n": "phaseB_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseB_active", "u": "J", "v": 1431288000.0}, {"n": "phaseB_reactive", "u": "J", "v": 159768000.0}, {"n": "phaseB_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "phaseC_voltage", "u": "V", "v": 221.0}, {"n": "phaseC_current", "u": "A", "v": 3.5499999999999998}, {"n": "phaseC_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseC_active", "u": "J", "v": 1368000000.0}, {"n": "phaseC_reactive", "u": "J", "v": 121931999.99999999}, {"n": "phaseC_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "gateway", "vs": "F8033202DF790000"}]', 'timestamp': '2023-02-16 02:31:37'}
    output = []
    time_matrix = []
    for item in payloadKSParser():
        payload = item.get("payload")
        time = item.get("time")
        # se tiver Accelerometer
        if "temperature" in payload:
            temperature = payload["temperature"]
            frequency = payload["frequency"]
            phaseA_voltage = payload["phaseA_voltage"]
            phaseA_current = payload["phaseA_current"]
            phaseA_pwr_factor = payload["phaseA_pwr_factor"]
            phaseA_active = payload["phaseA_active"]
            phaseA_reactive = payload["phaseA_reactive"]
            phaseA_tc_config = payload["phaseA_tc_config"]
            phaseB_voltage = payload["phaseB_voltage"]
            phaseB_current = payload["phaseB_current"]
            phaseB_pwr_factor = payload["phaseB_pwr_factor"]
            phaseB_active = payload["phaseB_active"]
            phaseB_reactive = payload["phaseB_reactive"]
            phaseB_tc_config = payload["phaseB_tc_config"]
            phaseC_voltage = payload["phaseC_voltage"]
            phaseC_current = payload["phaseC_current"]
            phaseC_pwr_factor = payload["phaseC_pwr_factor"]
            phaseC_active = payload["phaseC_active"]
            phaseC_reactive = payload["phaseC_reactive"]
            phaseC_tc_config = payload["phaseC_tc_config"]
            
            output.append([temperature, frequency, phaseA_voltage, phaseA_current, phaseA_pwr_factor, phaseA_active, phaseA_reactive, phaseA_tc_config, phaseB_voltage, phaseB_current, phaseB_pwr_factor, phaseB_active, phaseB_reactive, phaseB_tc_config, phaseC_voltage, phaseC_current, phaseC_pwr_factor, phaseC_active, phaseC_reactive, phaseC_tc_config])
            
            dt = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            time_matrix.append(dt)

        return output , time_matrix


def KSToH5():
    output_matrix , time_matrix = KSToNumpy()
    with h5py.File("./saida/ks/payloadKS.h5", "w") as f:
        f.create_dataset("payload", data=output_matrix)
        f.create_dataset("time", data=time_matrix)

def KSToCsv():
    output_matrix , time_matrix = KSToNumpy()
    # criar um csv pra cada
    np.savetxt("./saida/ks/payloadKS.csv", output_matrix, delimiter=",")
    np.savetxt("./saida/ks/time.csv", time_matrix, delimiter=",")
    


def main():
    WiseToH5()
    WiseToCsv()
    HexToH5()
    HexToCsv()
    KSToH5()
    KSToCsv()

if __name__ == "__main__":
    main()
