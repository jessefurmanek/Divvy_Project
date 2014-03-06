station_raw_data = [
	["20", "Sheffield Ave & Kingsbury St", "41.90959193", "-87.65349723", "15", "154", "6/28/2013"],
	["349", "Halsted St & Wrightwood Ave", "41.929143", "-87.649077", "15", "210", "10/28/2013"]
];

stations = _(stations_raw).map(function (station_raw) {
    return {
        id: station_raw_data[0],
        name: station_raw_data[1],
        latitude: station_raw_data[2],
        longitude: station_raw_data[3]
        dpcapacity: station_raw_data[4]
        landmark: station_raw_data[5]
        online_date: station_raw_data[6]),
    }
};
