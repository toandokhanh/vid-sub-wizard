// const inputFile = document.querySelector("#file");
const inputSubmit = document.querySelector("#submit");
const modal = document.querySelector(".modal");
const form = document.querySelector(".index");
const form_loading = document.querySelector(".loading");
const select = document.querySelector("#language");
const viewSrt = document.querySelectorAll("tbody .view_srt");
const deleteSrt = document.querySelectorAll("tbody .delete_srt");
const dangki = document.querySelector(".dangky");
const change = document.querySelector(".change");
const flash = document.querySelector(".flash");



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
  if (form_loading) {
    form_loading.onsubmit = () => {
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
      const a = confirm(`Bạn có muốn xoá video ${data}!`);
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


$(document).ready(function() {
  $('textarea').focus(function() {
    // Lấy thời gian bắt đầu từ hàng chứa <textarea>
    var start_time = $(this).closest('tr').find('input[name^="start_"]').val();
    // Tìm đối tượng video và thiết lập thời gian hiển thị
    var video = $('video')[0];
    video.currentTime = convertTimeToSeconds(start_time);
    // video.play();
  });
  
  // Hàm chuyển đổi định dạng thời gian sang giây
  function convertTimeToSeconds(time) {
    var parts = time.split(':');
    var hour = parseInt(parts[0]);
    var minute = parseInt(parts[1]);
    var second = parseFloat(parts[2].replace(',', '.'));
    console.log(second);
    second = second + 0.06;
    console.log(second);
    return hour * 3600 + minute * 60 + second;
  }
});

