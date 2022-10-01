import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  baseApiUrl = "http://localhost:8000/process"

  constructor(private http : HttpClient) { }


  sendId(id:String) {
    return this.http.get(this.baseApiUrl+"/"+id)
  }


}
