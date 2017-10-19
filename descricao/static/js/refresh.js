function autoRefresh(interval) {
	setTimeout("atualizar();",interval);
}
function atualizar() {
  // faz a lógica desejada...
}


/* Exemplo abaixo de como chamar a função na página em HTML

</script>
<title>Titulo...</title></head>
<body onload="javascript:autoRefresh(6000);">
<p>executará a função a cada 6 segundos...
</body>
</html>

Aqui termina ...*/
