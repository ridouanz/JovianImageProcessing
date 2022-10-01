import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  isHidden1 = false;
  isHidden2 = false;
  constructor() { }

  ngOnInit(): void {
  }

  onSubmit(f: NgForm ) {

  }
}
