from payloadHex import payloadHexParser
from payloadWise import payloadWiseParser
from payloadKs import payloadKSParser
import h5py
import numpy as np
import pandas as pd
from datetime import datetime
import json


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

            x_matrix.append(
                [
                    x["OAVelocity"],
                    x["Peakmg"],
                    x["RMSmg"],
                    x["Kurtosis"],
                    x["CrestFactor"],
                    x["Skewness"],
                    x["Deviation"],
                    x["Peak-to-Peak Displacement"],
                    time,
                ]
            )
            y_matrix.append(
                [
                    y["OAVelocity"],
                    y["Peakmg"],
                    y["RMSmg"],
                    y["Kurtosis"],
                    y["CrestFactor"],
                    y["Skewness"],
                    y["Deviation"],
                    y["Peak-to-Peak Displacement"],
                    time,
                ]
            )
            z_matrix.append(
                [
                    z["OAVelocity"],
                    z["Peakmg"],
                    z["RMSmg"],
                    z["Kurtosis"],
                    z["CrestFactor"],
                    z["Skewness"],
                    z["Deviation"],
                    z["Peak-to-Peak Displacement"],
                    time,
                ]
            )
    x_matrix = np.array(x_matrix)
    y_matrix = np.array(y_matrix)
    z_matrix = np.array(z_matrix)

    return x_matrix, y_matrix, z_matrix


def WiseToPandas():
    x_matrix, y_matrix, z_matrix = WiseToNumpy()
    x_df = pd.DataFrame(
        x_matrix,
        columns=[
            "OAVelocity",
            "Peakmg",
            "RMSmg",
            "Kurtosis",
            "CrestFactor",
            "Skewness",
            "Deviation",
            "Peak-to-Peak Displacement",
            "Time",
        ],
    )
    y_df = pd.DataFrame(
        y_matrix,
        columns=[
            "OAVelocity",
            "Peakmg",
            "RMSmg",
            "Kurtosis",
            "CrestFactor",
            "Skewness",
            "Deviation",
            "Peak-to-Peak Displacement",
            "Time",
        ],
    )
    z_df = pd.DataFrame(
        z_matrix,
        columns=[
            "OAVelocity",
            "Peakmg",
            "RMSmg",
            "Kurtosis",
            "CrestFactor",
            "Skewness",
            "Deviation",
            "Peak-to-Peak Displacement",
            "Time",
        ],
    )

    return x_df, y_df, z_df


def WiseToH5():
    x_matrix, y_matrix, z_matrix = WiseToPandas()
    # converter as colunas do DataFrame para tipos suportados pelo HDF5
    x_matrix = x_matrix.astype("float64")
    y_matrix = y_matrix.astype("float64")
    z_matrix = z_matrix.astype("float64")

    with h5py.File("wise_data.h5", "w") as f:
        # criar conjuntos de dados para cada matriz de dados
        f.create_dataset("x", data=x_matrix)
        f.create_dataset("y", data=y_matrix)
        f.create_dataset("z", data=z_matrix)


def WiseToCsv():
    x_matrix, y_matrix, z_matrix = WiseToPandas()
    columns = [
        "OAVelocity",
        "Peakmg",
        "RMSmg",
        "Kurtosis",
        "CrestFactor",
        "Skewness",
        "Deviation",
        "Peak-to-Peak Displacement, Time",
    ]

    # criar um arquivo pra cada
    with open("./saida/wise/x.csv", "w") as f:
        x_matrix.to_csv(f, index=False, header=True)

    with open("./saida/wise/y.csv", "w") as f:
        y_matrix.to_csv(f, index=False, header=True)

    with open("./saida/wise/z.csv", "w") as f:
        z_matrix.to_csv(f, index=False, header=True)


def HexToNumpy():
    # {"InletPressure": 16.93051528930664, "OutletPressure": 1011.0496215820312, "OutletTemperature": 83.23367309570312, "InverterSpeed": 4558.0}', 'timestamp': '2023-02-16 02:30:36'}
    output = []
    time_matrix = []
    payloadHexParserData = payloadHexParser()
    if payloadHexParserData == None:
        return None

    for item in payloadHexParserData:
        payload = item.get("payload")
        time = item.get("time")
        # se tiver Accelerometer
        if "InletPressure" in payload:
            inletPressure = payload["InletPressure"]
            outletPressure = payload["OutletPressure"]
            outletTemperature = payload["OutletTemperature"]
            inverterSpeed = payload["InverterSpeed"]
            output.append(
                [inletPressure, outletPressure, outletTemperature, inverterSpeed, time]
            )
            dt = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            time_matrix.append(dt)

    output_matrix = np.array(output)
    time_matrix = np.array(time_matrix, dtype="datetime64[ns]")
    time_matrix = time_matrix.astype("int64")
    return output_matrix


def HexToPandas():
    output_matrix = HexToNumpy()
    df = pd.DataFrame(
        output_matrix,
        columns=[
            "InletPressure",
            "OutletPressure",
            "OutletTemperature",
            "InverterSpeed",
            "Time",
        ],
    )
    return df


def HexToH5():
    output_matrix = HexToNumpy()
    with h5py.File("./saida/hex/payloadHex.h5", "w") as f:
        f.create_dataset("payload", data=output_matrix)


def HexToCsv():
    output_matrix = HexToPandas()
    with open("./saida/hex/payloadHex.csv", "w") as f:
        output_matrix.to_csv(f, index=False, header=True)


def KSToNumpy():
    # {"n": "temperature", "u": "Cel", "v": 52.0}, {"n": "frequency", "u": "Hz", "v": 60.0}, {"n": "phaseA_voltage", "u": "V", "v": 221.5}, {"n": "phaseA_current", "u": "A", "v": 3.5}, {"n": "phaseA_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseA_active", "u": "J", "v": 1362168000.0}, {"n": "phaseA_reactive", "u": "J", "v": 195624000.0}, {"n": "phaseA_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "phaseB_voltage", "u": "V", "v": 221.09999999999999}, {"n": "phaseB_current", "u": "A", "v": 3.6000000000000001}, {"n": "phaseB_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseB_active", "u": "J", "v": 1431288000.0}, {"n": "phaseB_reactive", "u": "J", "v": 159768000.0}, {"n": "phaseB_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "phaseC_voltage", "u": "V", "v": 221.0}, {"n": "phaseC_current", "u": "A", "v": 3.5499999999999998}, {"n": "phaseC_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseC_active", "u": "J", "v": 1368000000.0}, {"n": "phaseC_reactive", "u": "J", "v": 121931999.99999999}, {"n": "phaseC_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "gateway", "vs": "F8033202DF790000"}]', 'timestamp': '2023-02-16 02:31:37'}
    output = []
    for item in payloadKSParser():
        # [{'bn': 'F80332060002BD7B', 'bt': 1676514561}, {'n': 'uplink', 'u': 'count', 'v': 1585}, {'n': 'activation_mode', 'vs': 'ABP'}, {'n': 'datarate', 'vs': 'SF12BW125'}, {'n': 'rssi', 'u': 'dBW', 'v': -90}, {'n': 'snr', 'u': 'dB', 'v': 7.8}, {'n': 'model', 'vs': 'ite11li'}, {'n': 'version', 'vs': '1.0.3.0'}, {'n': 'temperature', 'u': 'Cel', 'v': 52.0}, {'n': 'frequency', 'u': 'Hz', 'v': 60.0}, {'n': 'phaseA_voltage', 'u': 'V', 'v': 221.8}, {'n': 'phaseA_current', 'u': 'A', 'v': 3.5}, {'n': 'phaseA_pwr_factor', 'u': '/', 'v': 0.8600000000000001}, {'n': 'phaseA_active', 'u': 'J', 'v': 1362168000.0}, {'n': 'phaseA_reactive', 'u': 'J', 'v': 195624000.0}, {'n': 'phaseA_tc_config', 'vs': 'POWCT-T16-150-333'}, {'n': 'phaseB_voltage', 'u': 'V', 'v': 221.3}, {'n': 'phaseB_current', 'u': 'A', 'v': 3.6}, {'n': 'phaseB_pwr_factor', 'u': '/', 'v': 0.8799999999999999}, {'n': 'phaseB_active', 'u': 'J', 'v': 1431288000.0}, {'n': 'phaseB_reactive', 'u': 'J', 'v': 159768000.0}, {'n': 'phaseB_tc_config', 'vs': 'POWCT-T16-150-333'}, {'n': 'phaseC_voltage', 'u': 'V', 'v': 221.3}, {'n': 'phaseC_current', 'u': 'A', 'v': 3.55}, {'n': 'phaseC_pwr_factor', 'u': '/', 'v': 0.8700000000000001}, {'n': 'phaseC_active', 'u': 'J', 'v': 1368000000.0}, {'n': 'phaseC_reactive', 'u': 'J', 'v': 121931999.99999999}, {'n': 'phaseC_tc_config', 'vs': 'POWCT-T16-150-333'}, {'n': 'gateway', 'vs': 'F8033202DF790000'}]
        try:
            payload = item.get("payload")
            print(payload)
            time = item.get("time")

            # pegar os valores
            temperatura = payload[8].get("v")
            frequencia = payload[9].get("v")
            faseA_tensao = payload[10].get("v")
            faseA_corrente = payload[11].get("v")
            faseA_fator_potencia = payload[12].get("v")
            faseA_ativa = payload[13].get("v")
            faseA_reativa = payload[14].get("v")
            faseA_config_tc = payload[15].get("vs")
            faseB_tensao = payload[16].get("v")
            faseB_corrente = payload[17].get("v")
            faseB_fator_potencia = payload[18].get("v")
            faseB_ativa = payload[19].get("v")
            faseB_reativa = payload[20].get("v")
            faseB_config_tc = payload[21].get("vs")
            faseC_tensao = payload[22].get("v")
            faseC_corrente = payload[23].get("v")
            faseC_fator_potencia = payload[24].get("v")
            faseC_ativa = payload[25].get("v")
            faseC_reativa = payload[26].get("v")
            faseC_config_tc = payload[27].get("vs")
        except IndexError:
            pass

        output.append(
            [
                temperatura,
                frequencia,
                faseA_tensao,
                faseA_corrente,
                faseA_fator_potencia,
                faseA_ativa,
                faseA_reativa,
                faseA_config_tc,
                faseB_tensao,
                faseB_corrente,
                faseB_fator_potencia,
                faseB_ativa,
                faseB_reativa,
                faseB_config_tc,
                faseC_tensao,
                faseC_corrente,
                faseC_fator_potencia,
                faseC_ativa,
                faseC_reativa,
                faseC_config_tc,
                time,
            ]
        )
    return output


def KSToPandas():
    output_matrix = KSToNumpy()
    columns = [
        "temperature",
        "frequency",
        "phaseA_voltage",
        "phaseA_current",
        "phaseA_pwr_factor",
        "phaseA_active",
        "phaseA_reactive",
        "phaseA_tc_config",
        "phaseB_voltage",
        "phaseB_current",
        "phaseB_pwr_factor",
        "phaseB_active",
        "phaseB_reactive",
        "phaseB_tc_config",
        "phaseC_voltage",
        "phaseC_current",
        "phaseC_pwr_factor",
        "phaseC_active",
        "phaseC_reactive",
        "phaseC_tc_config",
        "time",
    ]
    df = pd.DataFrame(output_matrix, columns=columns)

    return df


def KSToH5():
    output_matrix = KSToNumpy()
    with h5py.File("./saida/ite/payloadITE.h5", "w") as f:
        f.create_dataset("payload", data=output_matrix)


def KSToCsv():
    output_matrix = KSToPandas()
    with open("./saida/ite/payloadITE.csv", "w") as f:
        output_matrix.to_csv(f, index=False, header=True)


def toH5AndCsv():
    # WiseToCsv()
    # HexToCsv()
    # KSToCsv()
    WiseToH5()
    print("WiseToH5")
    HexToH5()
    print("HexToH5")
    KSToH5()
    print("KSToH5")


def main():
    # WiseToCsv()
    # HexToCsv()
    KSToCsv()
    # WiseToH5()
    # HexToH5()
    # KSToH5()


if __name__ == "__main__":
    main()
