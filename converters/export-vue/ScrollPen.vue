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
    <path d="m8,21c-1.1,0-2-.9-2-2V5c0-1.1-.9-2-2-2s-2,.9-2,2v3h4" /><path d="m20,7v-2c0-1.1-.9-2-2-2H4" /><path d="m18.4,11.62c.83-.83,2.17-.83,3,0s.83,2.17,0,3l-5.4,5.4-4,1,1-4,5.4-5.4Z" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>