import {
	moveHandler,
	downHandler,
	upHandler,
	setCanvas,
	reset
} from "./draw.js";
import { upload } from "./upload.js";

const dataURItoBlob = (dataURI) => {
	const byteString = atob(dataURI.split(',')[1]);

	// separate out the mime component
	const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

	// write the bytes of the string to an ArrayBuffer
	const ab = new ArrayBuffer(byteString.length);
	const ia = new Uint8Array(ab);
	for (var i = 0; i < byteString.length; i++) {
		ia[i] = byteString.charCodeAt(i);
	}
	return new Blob([ia], {type: mimeString});
};

const captureHandler = (evnet) => {
	const data = document.getElementById('mycanvas').toDataURL('image/png');
	const blob = dataURItoBlob(data);
	const formData = new FormData();
	formData.append("image", blob);
	
	upload(formData, $("#convert-draw").next()[0], $("#convert-draw")[0]);
};

$(document).ready(() => {
	const canvas = document.getElementById("mycanvas");
	const ctx = canvas.getContext("2d");

	let img;

	setCanvas(ctx, canvas);

	ctx.fillStyle = '#ffffff';
	ctx.fillRect(0, 0, 256, 256);

	$("#convert-draw").on("click", captureHandler)

	$("#reset").on("click", reset);

	$("input").on("input", (event) => {
		img = Array.from(event.target.files)[0]
		$("img").eq(0).attr("src", URL.createObjectURL(img));
	});

	$("#convert-upload").on("click", () => {
		const formData = new FormData();
		formData.append("image", img);
		
		upload(formData, $("#convert-upload").next()[0], $("#convert-upload")[0]);
	});

	$(canvas).on("mousemove", moveHandler);
	$(canvas).on("mousedown", downHandler);
	$(canvas).on("mouseup", upHandler);
});