// // let inputFile = document.querySelector("#file");
let inputSubmit = document.querySelector("#submit");
let modal = document.querySelector(".modal");
let form = document.querySelector(".index");
let select = document.querySelector("#language");
let viewSrt = document.querySelectorAll("tbody .view_srt");
let deleteSrt = document.querySelectorAll("tbody .delete_srt");
let dangki = document.querySelector(".dangky");
let change = document.querySelector(".change");
flash = document.querySelector(".flash");

window.onload = () => {
  if (flash) {
    setTimeout(() => {
      flash.classList.add("hidden");
    }, 3000);
  }
  if (form) {
    form.onsubmit = () => {
      // if (select.value == "None") {
      //   // alert("Hi");
      // }
      modal.classList.add("active");
    };
  }
};

if (viewSrt) {
  viewSrt.forEach((item) => {
    item.onclick = () => {
      trElement = item.parentElement.parentElement;
      fileSrt = trElement.firstElementChild;
      nameSrt = fileSrt.textContent.slice(13);
      nameMp4 = nameSrt.replace(".srt", ".mp4");

      location.href = `/loading/${nameMp4}`;
    };
  });
}

if (deleteSrt) {
  deleteSrt.forEach((item) => {
    item.onclick = () => {
      data = item.dataset.name;
      let a = confirm(`Bạn có muốn xoá video ${data}!`);
      if (a) {
        location.href = `/xoa/${data}`;
      }
    };
  });
}

if (change) {
  change.onclick = () => {
    if (change.dataset.nn) {
      nn = change.dataset.nn;
      value = change.dataset.name;
      mp4 = value.split("/")[1];
      name_file = mp4.split(".")[0];
      nn1 = nn.split("/")[0];
      nn2 = nn.split("/")[1];
      if (nn1 == nn2) {
        change.style.display = "none";
      }
      if (nn1 != nn2) {
        change.style.display = "block";

        if (window.location.href.includes("_out.mp4")) {
          a = window.location.href.replace("_out.mp4", ".mp4");
          window.location.href = a;
        } else {
          window.location.href = `/loading/${name_file}_out.mp4`;
        }
      }
    }
  };
}
