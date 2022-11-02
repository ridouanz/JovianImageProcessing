import { Injectable } from '@angular/core';
import { SafeResourceUrl } from '@angular/platform-browser';
import { ImageResponse } from '../shared/image-response';

@Injectable({
  providedIn: 'root'
})
export class ParentService {

   list : any;

  constructor() { }


  updateImagesInComponents(list :  [string,string,SafeResourceUrl,SafeResourceUrl]) {
      this.list = list;
  } 
  getImagesTrustedLinks() {
    return this.list;
  }
}
