export function upload(data, imgElement, button) {
	imgElement.src = '/static/img/loading.gif';
	button.disabled = true;
	$.ajax({
		url: '/upload',
		type: 'POST',
		data: data,
		processData: false,
		contentType: false,
		responseType: 'blob',
		success: function(response) {
			imgElement.src = 'data:image/png;base64,' + response;;
			button.disabled = false;
		},
		error: function(xhr, status, error) {
			console.error('업로드 실패:', error);
			imgElement.src = '';
			button.disabled = false;
		}
	});
}