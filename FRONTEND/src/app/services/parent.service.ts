import { Injectable } from '@angular/core';
import { ImageResponse } from '../shared/image-response';
import { BrowserModule, DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Injectable({
  providedIn: 'root'
})
export class ParentService {

   list : any;
   urlToTrust_old = "../../assets/imgs/";
  urlToTrust_new = "../../assets/processed_imgs/";

  constructor(private sanitizer: DomSanitizer) { }


  updateUrls(resp_after_processing : ImageResponse | undefined) {
    let trustedLinks : [SafeResourceUrl,SafeResourceUrl] ;
    this.urlToTrust_old =  this.urlToTrust_old + resp_after_processing?.old + "";
    this.urlToTrust_new =  this.urlToTrust_new + resp_after_processing?.new + "";

    let trustedUrl_old =
        this.sanitizer.bypassSecurityTrustResourceUrl(this.urlToTrust_old.toString());
   let trustedUrl_new =
        this.sanitizer.bypassSecurityTrustResourceUrl(this.urlToTrust_new.toString());  

    this.updateImagesInComponents([trustedUrl_old,trustedUrl_new]);
     
  }

  updateImagesInComponents(list :  [SafeResourceUrl,SafeResourceUrl]) {
      this.list = list;
  } 

  
  getImagesTrustedLinks() {
    return this.list;
  }
}
