document.addEventListener('DOMContentLoaded', function() {
    // Inicializar mapa
    var map = L.map('mapa-denuncias').setView([-23.550520, -46.633309], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Variáveis globais
    var markers = [];
    var detalheModal = new bootstrap.Modal(document.getElementById('detalheModal'));

    // Cores para os tipos de problemas
    var cores = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#33FFF5', '#F5FF33'];

    // Solicitar localização do usuário
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            map.setView([position.coords.latitude, position.coords.longitude], 15);
            carregarDenuncias();
        }, function(error) {
            console.error("Erro ao obter localização:", error);
            carregarDenuncias();
        });
    } else {
        console.log("Geolocalização não disponível");
        carregarDenuncias();
    }

    // Função para carregar denúncias
    function carregarDenuncias() {
        // Limpar marcadores existentes
        markers.forEach(function(marker) {
            map.removeLayer(marker);
        });
        markers = [];

        // Construir URL com filtros
        var url = '/mapa/api/denuncias/?';
        var tipo = document.getElementById('filtro-tipo').value;
        var dataInicio = document.getElementById('filtro-data-inicio').value;
        var dataFim = document.getElementById('filtro-data-fim').value;

        if (tipo) url += 'tipo=' + tipo + '&';
        if (dataInicio) url += 'data_inicio=' + dataInicio + '&';
        if (dataFim) url += 'data_fim=' + dataFim + '&';

        // Fazer requisição AJAX
        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Atualizar estatísticas
                document.getElementById('total-denuncias').textContent = data.denuncias.length;
                document.getElementById('visualizando-denuncias').textContent = data.denuncias.length;

                // Adicionar marcadores
                data.denuncias.forEach(function(denuncia) {
                    var corIndex = denuncia.tipo_problema_id % cores.length;
                    var icone = L.divIcon({
                        className: 'custom-div-icon',
                        html: `<div style="background-color: ${cores[corIndex]};" class="marker-pin"></div>`,
                        iconSize: [30, 42],
                        iconAnchor: [15, 42]
                    });

                    var marker = L.marker([denuncia.latitude, denuncia.longitude], {icon: icone}).addTo(map);
                    marker.bindPopup(`
                        <strong>${denuncia.descricao}</strong><br>
                        Tipo: ${denuncia.tipo_problema}<br>
                        Data: ${denuncia.data_hora}<br>
                        <a href="#" onclick="abrirDetalhes(${denuncia.id}); return false;">Ver detalhes</a>
                    `);

                    markers.push(marker);
                });
            })
            .catch(error => console.error('Erro ao carregar denúncias:', error));
    }

    // Função para abrir detalhes
    window.abrirDetalhes = function(id) {
        fetch('/mapa/denuncia/' + id + '/')
            .then(response => response.text())
            .then(html => {
                document.getElementById('detalhe-conteudo').innerHTML = html;
                detalheModal.show();
            });
    }

    // Event listeners
    document.getElementById('filtro-form').addEventListener('submit', function(e) {
        e.preventDefault();
        carregarDenuncias();
    });
});
