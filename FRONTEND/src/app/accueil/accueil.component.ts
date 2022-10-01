import { Component, OnInit } from '@angular/core';
import Typewriter from 'node_modules/t-writer.js';

@Component({
  selector: 'app-accueil',
  templateUrl: './accueil.component.html',
  styleUrls: ['./accueil.component.css']
})
export class AccueilComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    const target = document.querySelector('.description')

  const options = {
    loop: true
  }
    const writer = new Typewriter(target, {
      loop: true,
      typeSpeed: 150,
      deleteSpeed: 80,
      typeColor: '#fff',
    })
    
    writer
      .type('Here you can')
      .rest(2000)
      .changeOps({ deleteSpeed: 200 })
      .remove(4)
      .type('Explore Jupiter')
      .rest(2000)
      .remove(4)
      .type('process images')
      .rest(2000)
      .changeOps({ deleteSpeed: 200 })
      .remove(21)
      .type('recoginition')
      .rest(2000)
      .clear()
      .start()
          
  }

}
