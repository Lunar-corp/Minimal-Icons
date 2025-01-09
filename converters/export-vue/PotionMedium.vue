<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="m19,15h0c0,3.87-3.13,7-7,7h0c-3.87,0-7-3.13-7-7h0c0-3.18,2.11-5.85,5-6.71V2h4v6.29c1.13.33,2.14.95,2.95,1.76,1.27,1.27,2.05,3.01,2.05,4.95Z" /><line x1="16" y1="2" x2="14" y2="2" /><line x1="10" y1="2" x2="8" y2="2" /><path d="m6,15c2,0,2,1,4,1s2-1,4-1,2,1,4,1" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>