import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { FormControl } from '@angular/forms';
import { FormGroup, Validators} from '@angular/forms';
import { FileUploadService } from '../services/file-upload.service';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  // Variable to store shortLink from api response
	shortLink: string = "";
	loading: boolean = false; // Flag variable
	file : any;// Variable to store file

  isHidden = false;
  isHidden2 = false;

  
  constructor(private fileUploadService: FileUploadService) { }

  ngOnInit(): void {
  }

  // On file Select
	onChange(event : any) {
		this.file = event.target.files[0];
	}

  // OnClick of button Upload
	onUpload() {
		this.loading = !this.loading;
		console.log(this.file);
		this.fileUploadService.upload(this.file).subscribe(
			(event: any) => {
				if (typeof (event) === 'object') {

					// Short link via api response
					this.shortLink = event.link;

					this.loading = false; // Flag variable
				}
			}
		);
	}

  
  onSubmit(f: NgForm ) {
    console.log(f.form.value)

  }

  onSubmit2(f: NgForm ) {
    console.log(f.form.value)

  }

  makeHide(a : number){
    if(a === 1) {
      this.isHidden = true;
      this.isHidden2 = false;
    } else {
      this.isHidden = false;
      this.isHidden2 = true;
    }
  }
}
