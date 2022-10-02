import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { ImageId } from '../shared/image-id';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  baseApiUrl = "http://localhost:8000/process"

  constructor(private http : HttpClient) { }


  sendId(id:String) : Observable<ImageId> {

    return this.http.get<ImageId>(this.baseApiUrl+"/"+id).pipe(
      map(result => {return result})
    );
  }


}
