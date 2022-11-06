import { Component, Input, OnInit } from '@angular/core';
import { SafeResourceUrl } from '@angular/platform-browser';
import { ParentService } from '../services/parent.service';

@Component({
  selector: 'app-processing',
  templateUrl: './processing.component.html',
  styleUrls: ['./processing.component.css']
})
export class ProcessingComponent implements OnInit {

   list : any;
   process_old : SafeResourceUrl | undefined ;
   process_new : SafeResourceUrl | undefined;

  constructor(private sharedService : ParentService) { 
  }


  
  ngOnInit(): void {
    this.setProcessImgProperties();
  }

  setProcessImgProperties() {

    this.list = this.sharedService.getImagesTrustedLinks();
    this.process_old = this.list[2];
    this.process_new = this.list[3];
  }

}
