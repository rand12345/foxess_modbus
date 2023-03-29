"""Inverter sensor"""
import logging

from custom_components.foxess_modbus.entities.modbus_integration_sensor import (
    ModbusIntegrationSensorDescription,
)
from custom_components.foxess_modbus.entities.validation import Min
from custom_components.foxess_modbus.entities.validation import Range
from homeassistant.components.number import NumberDeviceClass
from homeassistant.components.number import NumberMode
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import UnitOfTime

from .entity_factory import EntityFactory
from .modbus_number import ModbusNumberDescription
from .modbus_select import ModbusSelectDescription
from .modbus_sensor import ModbusSensorDescription

_LOGGER: logging.Logger = logging.getLogger(__package__)

H1: list[EntityFactory] = [
    ModbusSensorDescription(
        key="pv1_voltage",
        address=11000,
        name="PV1 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Range(0, 1000)],
    ),
    ModbusSensorDescription(
        key="pv1_current",
        address=11001,
        name="PV1 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="pv1_power",
        address=11002,
        name="PV1 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(0, 10000)],
    ),
    ModbusIntegrationSensorDescription(
        key="pv1_energy_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="PV1 Power Total",
        round_digits=2,
        source_entity="pv1_power",
        unit_time=UnitOfTime.HOURS,
    ),
    ModbusSensorDescription(
        key="pv2_voltage",
        address=11003,
        name="PV2 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Range(0, 1000)],
    ),
    ModbusSensorDescription(
        key="pv2_current",
        address=11004,
        name="PV2 Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="pv2_power",
        address=11005,
        name="PV2 Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(0, 10000)],
    ),
    ModbusIntegrationSensorDescription(
        key="pv2_energy_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="PV2 Power Total",
        round_digits=2,
        source_entity="pv2_power",
        unit_time=UnitOfTime.HOURS,
    ),
    # These probably also apply to the AC1, but that's currently untested
    ModbusSensorDescription(
        key="solar_energy_total",
        address=11070,
        name="Solar Generation Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="solar_energy_today",
        address=11071,
        name="Solar Generation Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="battery_charge_total",
        address=11073,
        name="Battery Charge Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="battery_charge_today",
        address=11074,
        name="Battery Charge Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="battery_discharge_total",
        address=11076,
        name="Battery Discharge Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="battery_discharge_today",
        address=11077,
        name="Battery Discharge Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="feed_in_energy_total",
        address=11079,
        name="Feed-in Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="feed_in_energy_today",
        address=11080,
        name="Feed-in Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="grid_consumption_energy_total",
        address=11082,
        name="Grid Consumption Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        # reported as overflowing
        # https://github.com/nathanmarlor/foxess_modbus/pull/91#issuecomment-1488266553
        # validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="grid_consumption_energy_today",
        address=11083,
        name="Grid Consumption Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="total_yield_total",
        address=11085,
        name="Yield Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        # currently overflows
        # validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="total_yield_today",
        address=11086,
        name="Yield Today",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        native_unit_of_measurement="kWh",
        scale=0.1,
        # unsure if this actually goes negative
        validate=[Range(-100, 100)],
    ),
]

AC1: list[EntityFactory] = [
    ModbusIntegrationSensorDescription(
        key="grid_consumption_energy_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="Grid Consumption Total",
        round_digits=2,
        source_entity="grid_consumption",
        unit_time=UnitOfTime.HOURS,
    ),
    ModbusIntegrationSensorDescription(
        key="feed_in_energy_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="Feed-in Total",
        round_digits=2,
        source_entity="feed_in",
        unit_time=UnitOfTime.HOURS,
    ),
    ModbusIntegrationSensorDescription(
        key="battery_charge_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="Battery Charge Total",
        round_digits=2,
        source_entity="battery_charge",
        unit_time=UnitOfTime.HOURS,
    ),
    ModbusIntegrationSensorDescription(
        key="battery_discharge_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="Battery Discharge Total",
        round_digits=2,
        source_entity="battery_discharge",
        unit_time=UnitOfTime.HOURS,
    ),
]

H1_AC1: list[EntityFactory] = [
    ModbusSensorDescription(
        key="invbatvolt",
        address=11006,
        name="Inverter Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="invbatpower",
        address=11007,
        name="Inverter Battery Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.01,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="battery_discharge",
        address=11008,
        name="Battery Discharge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="battery_charge",
        address=11008,
        name="Battery Charge",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="rvolt",
        address=11009,
        name="Grid Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Range(0, 300)],
    ),
    ModbusSensorDescription(
        key="rcurrent",
        address=11010,
        name="Grid Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="rfreq",
        address=11014,
        name="Grid Frequency",
        device_class=SensorDeviceClass.FREQUENCY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="Hz",
        scale=0.01,
        validate=[Range(0, 60)],
    ),
    ModbusSensorDescription(
        key="eps_rvolt",
        address=11015,
        name="EPS Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Range(0, 300)],
    ),
    ModbusSensorDescription(
        key="grid_ct",
        address=11021,
        name="Grid CT",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="feed_in",
        address=11021,
        name="Feed-in",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: v if v > 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="grid_consumption",
        address=11021,
        name="Grid Consumption",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        post_process=lambda v: abs(v) if v < 0 else 0,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="ct2_meter",
        address=11022,
        name="CT2 Meter",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="load_power",
        address=11023,
        name="Load Power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="kW",
        scale=0.001,
        validate=[Range(-100, 100)],
    ),
    ModbusIntegrationSensorDescription(
        key="load_power_total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        integration_method="left",
        name="Load Power Total",
        round_digits=2,
        source_entity="load_power",
        unit_time=UnitOfTime.HOURS,
    ),
    ModbusSensorDescription(
        key="invtemp",
        address=11024,
        name="Inverter Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="ambtemp",
        address=11025,
        name="Ambient Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="batvolt",
        address=11034,
        name="Battery Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="V",
        scale=0.1,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bat_current",
        address=11035,
        name="Battery Current",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(-100, 100)],
    ),
    ModbusSensorDescription(
        key="battery_soc",
        address=11036,
        name="Battery SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_kwh_remaining",
        address=11037,
        name="BMS kWh Remaining",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.01,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="battery_temp",
        address=11038,
        name="Battery Temp",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_charge_rate",
        address=11041,
        name="BMS Charge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_discharge_rate",
        address=11042,
        name="BMS Discharge Rate",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="A",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_cell_temp_high",
        address=11043,
        name="BMS Cell Temp High",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_cell_temp_low",
        address=11044,
        name="BMS Cell Temp Low",
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="°C",
        scale=0.1,
        validate=[Range(0, 100)],
    ),
    ModbusSensorDescription(
        key="bms_cell_mv_high",
        address=11045,
        name="BMS Cell mV High",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bms_cell_mv_low",
        address=11046,
        name="BMS Cell mV Low",
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="mV",
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bms_cycle_count",
        address=11048,
        name="BMS Cycle Count",
        state_class=SensorStateClass.MEASUREMENT,
        validate=[Min(0)],
    ),
    ModbusSensorDescription(
        key="bms_watthours_total",
        address=11049,
        name="BMS Watthours Total",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        native_unit_of_measurement="kWh",
        scale=0.1,
        # currently overflows
        # validate=[Range(0, 100)]
    ),
    ModbusSelectDescription(
        key="work_mode",
        address=41000,
        name="Work Mode",
        options_map={0: "Self Use", 1: "Feed-in First", 2: "Back-up"},
    ),
    # Sensor kept for back compat
    ModbusSensorDescription(
        key="min_soc",
        address=41009,
        name="Min SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusNumberDescription(
        key="min_soc",
        address=41009,
        name="Min SoC",
        mode=NumberMode.BOX,
        native_min_value=10,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement="%",
        device_class=NumberDeviceClass.BATTERY,
        icon="mdi:battery-arrow-down",
        validate=[Range(0, 100)],
    ),
    # Sensor kept for back compat
    ModbusSensorDescription(
        key="max_soc",
        address=41010,
        name="Max SoC",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusNumberDescription(
        key="max_soc",
        address=41010,
        name="Max SoC",
        mode=NumberMode.BOX,
        native_min_value=10,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement="%",
        device_class=NumberDeviceClass.BATTERY,
        icon="mdi:battery-arrow-up",
        validate=[Range(0, 100)],
    ),
    # Sensor kept for back compat
    ModbusSensorDescription(
        key="min_soc_on_grid",
        address=41011,
        name="Min SoC (On Grid)",
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
        native_unit_of_measurement="%",
        validate=[Range(0, 100)],
    ),
    ModbusNumberDescription(
        key="min_soc_on_grid",
        address=41011,
        name="Min SoC (On Grid)",
        mode=NumberMode.BOX,
        native_min_value=10,
        native_max_value=100,
        native_step=1,
        native_unit_of_measurement="%",
        device_class=NumberDeviceClass.BATTERY,
        icon="mdi:battery-arrow-down",
        validate=[Range(0, 100)],
    ),
]
