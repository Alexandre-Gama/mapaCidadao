document.addEventListener('DOMContentLoaded', function() {
    // Inicializar mapa
    var map = L.map('map').setView([-23.550520, -46.633309], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var marker = null;

    // Solicitar localização automaticamente ao carregar a página
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;

            // Centralizar o mapa
            map.setView([latitude, longitude], 17);

            // Adicionar marcador
            if (marker) {
                map.removeLayer(marker);
            }
            marker = L.marker([latitude, longitude]).addTo(map);

            // Atualizar campos hidden
            document.getElementById('id_latitude').value = latitude;
            document.getElementById('id_longitude').value = longitude;

        }, function(error) {
            console.error("Erro ao obter localização:", error);
        });
    } else {
        console.log("Geolocalização não disponível");
    }

    // Adicionar marcador ao clicar no mapa
    map.on('click', function(e) {
        if (marker) {
            map.removeLayer(marker);
        }
        marker = L.marker(e.latlng).addTo(map);

        // Atualizar campos de latitude e longitude
        document.getElementById('id_latitude').value = e.latlng.lat;
        document.getElementById('id_longitude').value = e.latlng.lng;
    });

    // Botão para usar localização atual
    document.getElementById('btn-usar-minha-localizacao').addEventListener('click', function() {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var latitude = position.coords.latitude;
                var longitude = position.coords.longitude;

                // Centralizar o mapa
                map.setView([latitude, longitude], 17);

                // Adicionar marcador
                if (marker) {
                    map.removeLayer(marker);
                }
                marker = L.marker([latitude, longitude]).addTo(map);

                // Atualizar campos hidden
                document.getElementById('id_latitude').value = latitude;
                document.getElementById('id_longitude').value = longitude;

            }, function(error) {
                console.error("Erro ao obter localização:", error);
                alert("Não foi possível obter sua localização. Por favor, clique no mapa para indicar a posição.");
            });
        } else {
            alert("Seu navegador não suporta geolocalização. Por favor, clique no mapa para indicar a posição.");
        }
    });
});
